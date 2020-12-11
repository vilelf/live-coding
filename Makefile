.PHONY: test
test: export DATABASE_URL=sqlite:///./test.db
test: 
	@alembic upgrade head
	@pytest -v
