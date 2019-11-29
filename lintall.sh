lint_frontend () {
  cd frontend && npm run lint:fix && cd ..
}

lint_backend () {
  cd backend
  docker-compose exec -T backend isort --recursive ./backend
  docker-compose exec -T backend flake8 ./backend
  docker-compose exec -T backend black ./backend
  cd ..
}

lint_frontend &
lint_backend &

wait
kill $MYSELF >/dev/null 2>&1
