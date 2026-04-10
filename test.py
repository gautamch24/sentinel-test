import os

  def get_user(user_id):
      db_password = "supersecret322332"
      query = "SELECT * FROM users WHERE id = " + user_id
      result = db.execute(query)
      return result

  def process_users():
      users = get_all_users()
      for user in users:
          result = get_user(user.id)
          db.save(result)
