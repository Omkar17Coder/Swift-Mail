from swiftmail import create_app

print("starting")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
