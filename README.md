# BibleQL Client Examples

Examples of using the [BibleQL](https://bibleql.org) API with the official Ruby, Node.js and Python client libraries.

## Prerequisites

- A BibleQL API key (set as `BIBLEQL_API_KEY` in a `.env` file)

Create a `.env` file in the project root:

```
BIBLEQL_API_KEY=your_api_key_here
```

## Ruby Example

### Setup

```bash
bundle install
```

### Usage

```bash
ruby test.rb
```

The Ruby example ([test.rb](test.rb)) demonstrates:

- Configuring the client with an API key, default translation, and timeout
- Fetching a passage by reference
- Accessing the passage reference, text, verses, and translation ID

```ruby
require "dotenv/load"
require "bibleql"

BibleQL.configure do |config|
  config.api_key = ENV["BIBLEQL_API_KEY"]
  config.default_translation = "spa-bes"
  config.timeout = 60
end

client = BibleQL.client
passage = client.passage("Mateo 28:18-20")

puts passage.reference
puts passage.text
passage.verses
puts passage.translation_id
```

## Node.js Example

### Setup

```bash
npm install
```

### Usage

```bash
node test.js
```

The Node.js example ([test.js](test.js)) demonstrates:

- Creating a client with an API key, default translation, and timeout
- Fetching a passage by reference using async/await
- Accessing the passage reference, text, verses, and translation ID

```javascript
require("dotenv").config();
const { BibleQLClient } = require("bibleql-js");

const client = new BibleQLClient({
  apiKey: process.env.BIBLEQL_API_KEY,
  defaultTranslation: "spa-bes",
  timeout: 60000,
});

async function main() {
  const passage = await client.passage("Mateo 28:18-20");
  console.log("Reference:", passage.reference);
  console.log("Text:", passage.text);
  console.log("Translation:", passage.translationId);
  console.log("Verses:", passage.verses);
}

main().catch(console.error);
```

## Python Example

### Setup

Requires Python 3.10+ (`.tool-versions` pins 3.15 for asdf users).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

```bash
python test.py
```

The Python example ([test.py](test.py)) demonstrates:

- Loading the API key from `.env` with `python-dotenv` (the client reads `BIBLEQL_API_KEY` automatically)
- Creating a client with a default translation and timeout, used as a context manager
- Fetching a passage by reference and accessing its reference, text, verses, and translation ID
- Semantic search by meaning
- Concordance: every occurrence of a word, with per-testament counts (Python client only)

```python
from dotenv import load_dotenv

import bibleql

load_dotenv()

with bibleql.Client(default_translation="spa-bes", timeout=60) as client:
    passage = client.passage("Mateo 28:18-20")
    print("Reference:", passage.reference)
    print("Text:", passage.text)
    print("Translation:", passage.translation_id)
    print("Verses:", passage.verses)

    results = client.semantic_search("amor y perdon", translation="spa-rv1909", limit=5)
    for r in results:
        print(f"{r.verse.book_name} {r.verse.chapter}:{r.verse.verse} ({r.similarity})")

    page = client.concordance("misericordia", translation="spa-rv1909", first=5)
    print(f"{page.total_count} occurrences of {page.entry.surface_forms}")
```

## Libraries

- Ruby: [bibleql-ruby](https://rubygems.org/gems/bibleql-ruby)
- Node.js: [bibleql-js](https://www.npmjs.com/package/bibleql-js)
- Python: [bibleql](https://pypi.org/project/bibleql/)
