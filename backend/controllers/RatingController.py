import sqlite3

class RatingController:
    def __init__(self, db_path="bookmarked.db"):
        self._db_path = db_path

    def _check_permission_stub(self, user_id: int) -> bool:
        """
        TEMPORARY STUB: Replace this once PermissionManager is implemented.
        Currently allows all users to post ratings.
        """
        # You can add a simple check here for now, e.g., if user_id is not None
        return user_id is not None

    def apply_rating(self, user_id: int, book_id: int, value: int) -> bool:
        """
        Implementation of UC-11: Submit a Rating.
        """
        # Step 1: Use the local stub instead of the missing PermissionManager
        if not self._check_permission_stub(user_id):
            print(f"Action Denied: User {user_id} is not authorized.")
            return False

        # Step 2: Database Connection
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        try:
            # We use a transaction to ensure both updates happen or neither does
            # 1. Update the running sum and total count of ratings
            cursor.execute("""
                UPDATE books 
                SET total_ratings = total_ratings + 1, 
                    rating_sum = rating_sum + ? 
                WHERE id = ?""", (value, book_id))
            
            # 2. Recalculate the average stored on the Book entity
            cursor.execute("""
                UPDATE books 
                SET avg_rating = CAST(rating_sum AS FLOAT) / total_ratings 
                WHERE id = ?""", (book_id,))
            
            conn.commit()
            print(f"Success: Book {book_id} rated {value} stars by User {user_id}")
            return True
        except Exception as e:
            conn.rollback()
            print(f"Database Error in RatingController: {e}")
            return False
        finally:
            conn.close()

    def get_average_rating(self, book_id: int) -> float:
        """Helper for the RatingWidget to display current stats."""
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT avg_rating FROM books WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else 0.0