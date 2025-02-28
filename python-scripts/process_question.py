import sys
import psycopg2

def process_question(question):
    conn = psycopg2.connect(
        dbname="cdp_chatbot",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Simple logic: platform detect karo
    platforms = ["Segment", "mParticle", "Lytics", "Zeotap"]
    detected_platform = None
    for platform in platforms:
        if platform.lower() in question.lower():
            detected_platform = platform
            break

    if not detected_platform:
        return "Sorry, yeh sawal CDP se related nahi hai ya platform clear nahi hai."

    # Database se content fetch karo
    cur.execute("SELECT content FROM cdp_docs WHERE platform = %s", (detected_platform,))
    result = cur.fetchone()
    if result:
        # Yeh basic hai, real mein keywords match karo
        return f"{detected_platform} ke liye jawab: {result[0][:200]}..."
    return "Mujhe iska jawab nahi mila, thodi aur specific info do."

if __name__ == "__main__":
    question = sys.argv[1]
    print(process_question(question))