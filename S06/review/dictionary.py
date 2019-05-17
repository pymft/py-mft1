# movie = [100, "Whatever Works", "Woody Allen", 2009]
movie = {"id": 100, "year": 2009, "title": "Whatever Works", "director": "Woody Allen"}
print(movie["title"])
print(movie)
movie["writer"] = "Woody Allen"
print(movie)

print(movie.keys())
print(movie.values())
print(movie.items())
movie.update({"a": 1234, "b": 12323434})
print(movie)


# movie["title"]
print(movie.get("producer", "Unknown"))