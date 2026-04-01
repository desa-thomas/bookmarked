import sqlite3
class ActivityManager:
    def __init__(self, db_path="bookmarked.db"):
        self._db_path = db_path

    def get_global_feed(self) -> list:
        """
        Collection-level operation: Retrieves social activity for the ActivityFeedPage.
        """
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row  # Returns results as dictionaries
        cursor = conn.cursor()
        
        # Join with Users to get profile data for the feed
        query = """
            SELECT u.username, s.text, s.timestamp, s.id as update_id, s.likes 
            FROM status_updates s
            JOIN users u ON s.user_id = u.id
            ORDER BY s.timestamp DESC
            LIMIT 20
        """
        cursor.execute(query)
        updates = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return updates

    def register_like(self, user_id: int, update_id: int):
        """
        Object-level operation: UC-12 Social Features.
        """
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        try:
            # Check if already liked (Business Logic)
            cursor.execute("SELECT 1 FROM likes WHERE user_id = ? AND update_id = ?", (user_id, update_id))
            if cursor.fetchone():
                return False # Already liked

            # Increment like count on the update entity
            cursor.execute("UPDATE status_updates SET likes = likes + 1 WHERE id = ?", (update_id,))
            cursor.execute("INSERT INTO likes (user_id, update_id) VALUES (?, ?)", (user_id, update_id))
            
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            return False
        finally:
            conn.close()