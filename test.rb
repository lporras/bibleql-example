require "dotenv/load"
require "bibleql"

BibleQL.configure do |config|
  config.api_key = ENV["BIBLEQL_API_KEY"]
  config.default_translation = "spa-bes"      # optional, defaults to "eng-web"
  config.timeout = 60                         # optional, defaults to 30 seconds
end

client = BibleQL.client

passage = client.passage("Mateo 28:18-20")
puts passage.reference       # => "John 3:16"
puts passage.text            # => "For God so loved the world..."
passage.verses          # => [#<BibleQL::Verse ...>]
puts passage.translation_id  # => "eng-web"

puts "\nSemantic Search for 'amor y perdon' in Spanish RV1909 translation:"
results = client.semantic_search("amor y perdon", translation: "spa-rv1909", limit: 5)
# See all results
results.each do |r|
  puts "#{r.verse.book_name} #{r.verse.chapter}:#{r.verse.verse} (#{r.similarity}) - #{r.verse.text}"
end
