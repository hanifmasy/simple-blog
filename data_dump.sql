-- Create Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'regular') NOT NULL
);

-- Create BlogPosts table
CREATE TABLE BlogPosts (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    author_id INT,
    published_date DATE NOT NULL,
    status ENUM('draft', 'published') NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Users(user_id)
);

-- Create Comments table
CREATE TABLE Comments (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES BlogPosts(post_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create LikesDislikes table
CREATE TABLE LikesDislikes (
    like_dislike_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT,
    comment_id INT,
    user_id INT NOT NULL,
    reaction ENUM('like', 'dislike') NOT NULL,
    FOREIGN KEY (post_id) REFERENCES BlogPosts(post_id),
    FOREIGN KEY (comment_id) REFERENCES Comments(comment_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);


-- Dummy data for Users table
INSERT INTO Users (name, email, password, role) VALUES
('John Doe', 'john@example.com', 'password123', 'admin'),
('Alice Smith', 'alice@example.com', 'pass456', 'regular'),
('Bob Johnson', 'bob@example.com', 'secret', 'regular');

-- Dummy data for BlogPosts table
INSERT INTO BlogPosts (title, content, author_id, published_date, status) VALUES
('Introduction to SQL', 'This is a beginner-level guide to SQL.', 1, '2024-03-14', 'published'),
('Advanced SQL Techniques', 'Learn advanced SQL techniques for data analysis.', 2, '2024-03-15', 'published'),
('Getting Started with Python', 'A beginner-friendly tutorial on Python programming language.', 3, '2024-03-16', 'draft');

-- Dummy data for Comments table
INSERT INTO Comments (post_id, user_id, content, date_created) VALUES
(1, 2, 'Great article!', '2024-03-14 10:00:00'),
(1, 3, 'Very helpful, thanks!', '2024-03-14 11:30:00'),
(2, 1, 'I enjoyed reading this.', '2024-03-15 09:45:00');

-- Dummy data for LikesDislikes table
INSERT INTO LikesDislikes (post_id, user_id, reaction) VALUES
(1, 2, 'like'),
(1, 3, 'like'),
(2, 1, 'like');
