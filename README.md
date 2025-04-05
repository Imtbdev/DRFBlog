# 📝 Blog API using Django REST Framework

This project is a simple blog API built with Django REST Framework.  
It supports creating posts, adding comments, and retrieving them via clean RESTful endpoints.

---

## 🔗 API Routes Overview

![API Routes](https://prnt.sc/CE9dDgTYGpS3)

---

## ✍️ Create a Post

To create a post, send a `POST` request to `/api/v1/posts/` with a valid token and post data.

![Create Post](https://prnt.sc/kNE_x1h60RD1)

---

## 💬 Add a Comment to a Post

To create a comment, send a `POST` request to `/api/v1/comments/` with the required fields (`text`, `post`, etc.).

![Create Comment](https://prnt.sc/0It98aSn2GSt)

---

## 🔍 View a Comment

To retrieve a comment by its ID, use the endpoint `/api/v1/comments/<id>/`.

![View Comment](https://prnt.sc/GF4wdXdQ8DYT)

---

## 📖 View a Post with Its Comments

The post detail view includes all related comments via the nested serializer.

![Post with Comments](https://prnt.sc/74mHSHLcwude)

---