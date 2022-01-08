.PHONY: all
all: build run

.PHONY: build
build:
	docker build -t pyapi .

.PHONY: run
run:
	docker run --rm -v $(PWD):/app -p 5000:5000 -it pyapi bash -c "sh /app/init.sh"
