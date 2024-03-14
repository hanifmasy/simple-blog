# simple-blog

simple blogging platform that has the following requirements:
- Blog posts have a title, content, author, published date, and status.
- Users have a name, email, password, and role (admin or regular user).
- Users can write blog posts.
- Users can leave comments on blog posts.
- Users can like and dislike blog posts and comments.

- ## ERD

Here's a basic relational database schema design for the requirements you've provided:

1. **Tables:**
    - Users
    - BlogPosts
    - Comments
    - LikesDislikes (for both posts and comments)
    
2. **Users Table:**
    - user_id (Primary Key)
    - name
    - email
    - password
    - role (admin or regular user)

3. **BlogPosts Table:**
    - post_id (Primary Key)
    - title
    - content
    - author_id (Foreign Key referencing user_id in Users table)
    - published_date
    - status (e.g., draft, published)

4. **Comments Table:**
    - comment_id (Primary Key)
    - post_id (Foreign Key referencing post_id in BlogPosts table)
    - user_id (Foreign Key referencing user_id in Users table)
    - content
    - date_created

5. **LikesDislikes Table:**
    - like_dislike_id (Primary Key)
    - post_id (Foreign Key referencing post_id in BlogPosts table, or NULL if it's a comment)
    - comment_id (Foreign Key referencing comment_id in Comments table, or NULL if it's a post)
    - user_id (Foreign Key referencing user_id in Users table)
    - reaction (like or dislike)


```
  +--------------+             +--------------+
  |     Users    |             |  BlogPosts   |
  +--------------+             +--------------+
  | user_id [PK] |1 ------- * | post_id [PK] |
  |     name     |             |    title     |
  |    email     |             |   content    |
  |   password   |             |  author_id   |       
  |     role     |             |published_date|
  +--------------+             |   status     |
         |                     +--------------+
         |
         |1
         |
  +--------------+
  |   Comments   |
  +--------------+
  |comment_id [PK]|
  |  post_id [FK] |
  |  user_id [FK] |
  |   content    |
  | date_created |
  +--------------+
         |
         |0..1
         |
  +------------------+
  |  LikesDislikes   |
  +------------------+
  | like_dislike_id  |
  |   post_id [FK]   |
  | comment_id [FK]  |
  |  user_id [FK]    |
  |    reaction      |
  +------------------+
```

**Explanation:**
- Users table stores information about users including their name, email, password, and role.
- BlogPosts table stores blog posts with attributes such as title, content, author ID, published date, and status.
- Comments table stores comments made by users on blog posts with attributes like comment content, post ID, user ID, and date created.
- LikesDislikes table stores likes and dislikes made by users on both blog posts and comments. It includes the ID of the liked/disliked post/comment, the ID of the user who liked/disliked it, and the type of reaction.

