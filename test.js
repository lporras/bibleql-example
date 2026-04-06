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
