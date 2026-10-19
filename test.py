from dotenv import load_dotenv

import bibleql

load_dotenv()  # reads BIBLEQL_API_KEY from .env

# api_key defaults to the BIBLEQL_API_KEY environment variable
with bibleql.Client(
    default_translation="spa-bes",  # optional, defaults to "eng-web"
    timeout=60,  # optional, defaults to 30 seconds
) as client:
    passage = client.passage("Mateo 28:18-20")
    print("Reference:", passage.reference)  # => "Mateo 28:18-20"
    print("Text:", passage.text)
    print("Translation:", passage.translation_id)  # => "spa-bes"
    print("Verses:", passage.verses)  # => [Verse(book_id='MAT', ...), ...]

    print("\n--- Semantic Search --- 'amor y perdon'")
    results = client.semantic_search("amor y perdon", translation="spa-rv1909", limit=5)
    for r in results:
        print(f"{r.verse.book_name} {r.verse.chapter}:{r.verse.verse} ({r.similarity})")
        print(f"  {r.verse.text}")

    print("\n--- Concordance --- 'misericordia'")
    page = client.concordance("misericordia", translation="spa-rv1909", first=5)
    print(f"{page.total_count} occurrences of {page.entry.surface_forms}")
    print(
        f"Old Testament: {page.entry.occurrences_by_testament.old}, "
        f"New Testament: {page.entry.occurrences_by_testament.new}"
    )
    for occurrence in page.occurrences:
        verse = occurrence.verse
        print(f"  {verse.book_name} {verse.chapter}:{verse.verse} - {occurrence.context}")
