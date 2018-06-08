# printing
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % (formatter, formatter, formatter, formatter)
# single-quotes and double-quotes
print formatter % (
    "I had this thing.", "I had this thing.", "But it didn't sing.", "So I said goodnight."
)
