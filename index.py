import streamlit as st

def center_text(text, heading_level=2):
    st.markdown(f"""
    <div style="text-align: center;">
        <h{heading_level}><span class='colored'>{text}</span></h{heading_level}>
    </div>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="PyCraft | Home", page_icon="images/favicon.png", layout="wide")

st.markdown("""
    <style>
        .centered { text-align: center; }
        .colored {
            color: #FF5733; /* Change this to your desired color */
            font-weight: bold; /* Optional: Add bold styling */
        }
        .lore-text { font-style: italic; line-height: 1.5; display: block; margin: auto; text-align: center; }
        .screenshot-container { display: flex; justify-content: space-between; margin: 20px 0; }
        .screenshot-container img { width: 30%; border-radius: 10px; }
        .github-link {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px 0;
        }
        .github-link a {
            font-size: 20px;
            padding: 10px 20px;
            background-color: #333; /* GitHub's dark color */
            color: white; /* White text */
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .github-link a:hover {
            background-color: #555; /* Lighter shade on hover */
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.image("images/pycraft_title.png", use_container_width=True)  # Updated here

# LORE TEXT
center_text("A gust of wind rushes through the treetops...")

st.markdown("""
<span class='lore-text'>The sky stretches endlessly in all directions, a vast ocean of swirling clouds.  
High above the world, on an island that drifts through the heavens, a lone figure awakens.  
No memories, no clothes—just the feeling of cold air against bare skin and the soft rustling of leaves.  
The island is alive. Ancient trees stand tall, their roots gripping the floating earth.  
Strange markings are etched into the rocks, whispering of a forgotten past.  
The wind carries echoes of something lost, something waiting to be rediscovered.  
No signs of civilization. No paths to follow.  
Only the endless sky and the unshaken silence.  
**Why here? Why alone?**  
The answers may lie within the island itself—or far beyond the clouds.</span>
""", unsafe_allow_html=True)

st.markdown("""## <span class='colored'>Description</span>
In this innovative and immersive game, you awaken as a character on a mesmerizing floating island suspended in a vast,
otherworldly sky. The game introduces a unique control mechanism where your movements are guided by the direction of
your gaze—simply rotate your head, and the AI seamlessly detects where you’re looking, translating your real-world
motions into in-game navigation. This cutting-edge technology creates an intuitive and engaging experience, allowing
you to explore the island’s lush landscapes, mysterious structures, and hidden secrets with unparalleled fluidity.
As you delve deeper into this surreal environment, the game challenges you to solve puzzles, uncover lore, and interact
with the world in ways that feel natural and immersive, blending reality and virtual adventure like never before.
""", unsafe_allow_html=True)

# THREE SCREENSHOTS OF THE GAME IN A ROW
center_text("Screenshots and Media")

col1, col2 = st.columns(2)

with col1:
    st.image("images/screenshot1.jpg", use_container_width=True)

with col2:
    st.image("images/screenshot2.png", use_container_width=True)


# YOUTUBE VIDEO PLAYER (SMALLER SIZE)
st.markdown("""
<div style="display: flex; justify-content: center;">
    <iframe width="600" height="338" src="https://www.youtube.com/embed/blLLtdv4tvo" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen></iframe>
</div>
""", unsafe_allow_html=True)

center_text("Game Features & Information")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🟩 Controls")
        st.write("""
        - **Rotate your head** to move!!! 🍔
        """)

    with col2:
        st.markdown("### 🛠 Development Stack")
        st.write("""
        - **Python** 🐍  
        - **Pygame** 🎮  
        - **Streamlit for Web UI** 🌐  
        - **AWS as a server.**
        """)

    with col3:
        st.markdown("### 🌟 Support & Community")
        st.write("""
        The game is being done by Thomas More University students!
        Thanks to Stefan Botnari, Jeff Tielen, Denys Herasymchuk and Artem Kucheruk.
        """)

# GITHUB LINK
st.markdown("""
<div class="github-link">
    <a href="https://github.com/Ace-Qwer/discovery-week" target="_blank">View on GitHub</a>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""@ All rights reserved by <span class='colored'>Thomas More University</span>""", unsafe_allow_html=True)
with col2:
    st.image("images/pycraft_title.png", width=300)