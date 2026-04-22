import aiosqlite
from datetime import datetime
from typing import Optional, List, Dict, Any
from bot.config import DB_PATH, logger


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                joined_at TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS progress (
                user_id INTEGER,
                question_id INTEGER,
                status TEXT DEFAULT 'attempted',
                attempts_count INTEGER DEFAULT 0,
                last_attempt_at TEXT,
                PRIMARY KEY (user_id, question_id)
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS attempts (
                attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                question_id INTEGER,
                user_answer TEXT,
                is_correct INTEGER,
                created_at TEXT
            )
        """)
        await db.commit()
    logger.info("Database initialized at %s", DB_PATH)


async def get_or_create_user(user_id: int, username: Optional[str], first_name: Optional[str]):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT 1 FROM users WHERE user_id = ?", (user_id,)
        )
        row = await cursor.fetchone()
        if not row:
            await db.execute(
                "INSERT INTO users (user_id, username, first_name, joined_at) VALUES (?, ?, ?, ?)",
                (user_id, username or "", first_name or "", datetime.utcnow().isoformat()),
            )
            await db.commit()


async def record_attempt(user_id: int, question_id: int, user_answer: str, is_correct: bool):
    now = datetime.utcnow().isoformat()
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO attempts (user_id, question_id, user_answer, is_correct, created_at) VALUES (?, ?, ?, ?, ?)",
            (user_id, question_id, user_answer, 1 if is_correct else 0, now),
        )
        cursor = await db.execute(
            "SELECT attempts_count, status FROM progress WHERE user_id = ? AND question_id = ?",
            (user_id, question_id),
        )
        row = await cursor.fetchone()
        if row:
            new_count = row[0] + 1
            new_status = "solved" if is_correct else row[1]
            await db.execute(
                "UPDATE progress SET attempts_count = ?, status = ?, last_attempt_at = ? WHERE user_id = ? AND question_id = ?",
                (new_count, new_status, now, user_id, question_id),
            )
        else:
            status = "solved" if is_correct else "attempted"
            await db.execute(
                "INSERT INTO progress (user_id, question_id, status, attempts_count, last_attempt_at) VALUES (?, ?, ?, ?, ?)",
                (user_id, question_id, status, 1, now),
            )
        await db.commit()


async def get_user_stats(user_id: int, total_questions: int) -> Dict[str, Any]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT COUNT(*), SUM(is_correct) FROM attempts WHERE user_id = ?",
            (user_id,),
        )
        total_attempts, total_correct = await cursor.fetchone()
        total_attempts = total_attempts or 0
        total_correct = total_correct or 0

        cursor = await db.execute(
            "SELECT COUNT(*) FROM progress WHERE user_id = ? AND status = 'solved'",
            (user_id,),
        )
        solved = (await cursor.fetchone())[0] or 0

        cursor = await db.execute(
            """
            SELECT question_id, is_correct FROM attempts
            WHERE user_id = ?
            ORDER BY attempt_id DESC
            """,
            (user_id,),
        )
        rows = await cursor.fetchall()
        streak = 0
        for _, is_correct in rows:
            if is_correct:
                streak += 1
            else:
                break

        return {
            "total_attempts": total_attempts,
            "total_correct": total_correct,
            "solved": solved,
            "total_questions": total_questions,
            "completion_pct": round((solved / total_questions) * 100, 1) if total_questions else 0,
            "streak": streak,
        }


async def get_progress_for_user(user_id: int) -> List[int]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT question_id FROM progress WHERE user_id = ? AND status = 'solved'",
            (user_id,),
        )
        rows = await cursor.fetchall()
        return [r[0] for r in rows]
