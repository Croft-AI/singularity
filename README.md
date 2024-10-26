# Singularity
Converting unstructured data into structured formats

# Parsing Methods

The following approach allows for text on scanned documents to be extracted

```
file > pdf > image > llm > formatted output
```

```
file > pdf > image > llm > markdown > llm > formatted output
```

The following approach allows for less LLM-reliant method of extracted information

```
file > unstructured-parser > llm > markdown > llm > formatted output
```