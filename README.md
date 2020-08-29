# nlp-api
A Python API that provides simplified NLP feedback based on language inputs. API uses NLTK library.

# Usage #
To run locally: 
- Run **install-api.ps1** to install all dependencies.
- Run **run-api.ps1** to launch flask locally on port 3000.

URL:
**http://localhost:3000/nlp-api/v1**

To request NLP breakdown:
URL:   POST http://localhost:3000/nlp-api/v1
Request Body:
    {
        "text": "hello world"
    }

Response Body example:
    {
    "tags": [
        {
        "tag": "NN",
        "word": "hello"
        },
        {
        "tag": "NN",
        "word": "world"
        }
    ],
    "text": "hello world",
    "words": [
        "hello",
        "world"
    ]
    }

