# installation

install the package, including uvicorn server
```bash
pip install "fastapi[all]"

```


# run
```bash
uvicorn main:app --reload
```

# path decorators
- @app.post()
- @app.put()
- @app.delete()
- @app.options()
- @app.head()
- @app.patch()
- @app.trace()

# tips
- path operations are evaluated in order, you need to make sure that the path for `/users/me` is declared before the one for `/users/{user_id}`
- 