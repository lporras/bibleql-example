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
