# BibleQL Client Examples

Examples of using the [BibleQL](https://bibleql.com) API with the official Ruby and Node.js client libraries.

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

## Libraries

- Ruby: [bibleql-ruby](https://rubygems.org/gems/bibleql-ruby)
- Node.js: [bibleql-js](https://www.npmjs.com/package/bibleql-js)
