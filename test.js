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

  console.log("\n--- Semantic Search --- 'el amor de Dios'");
  const results = await client.semanticSearch("el amor de Dios", {
    limit: 5,
    translation: "spa-rv1909",
  });
  results.forEach((result) => {
    console.log(
      `${result.verse.bookName} ${result.verse.chapter}:${result.verse.verse} (similarity: ${result.similarity})`
    );
    console.log(`  ${result.verse.text}`);
  });
}

main().catch(console.error);
