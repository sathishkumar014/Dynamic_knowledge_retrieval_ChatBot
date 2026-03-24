from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("knowledge.txt") as f:
    docs = f.readlines()

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(docs)

def get_answer(query):
    q_vec = vectorizer.transform([query])
    sim = cosine_similarity(q_vec, tfidf)[0]

    # Top 2 matches
    top_indices = sim.argsort()[-2:][::-1]

    responses = []
    for i in top_indices:
        if sim[i] > 0.2:
            responses.append(f"{docs[i].strip()} (score: {sim[i]:.2f})")

    if not responses:
        return "I couldn't find relevant info. Try asking differently."

    return " | ".join(responses)