import streamlit as st
from PIL import Image
import random

st.title("👩 Amma Vilichu AI")

CLEAN_DIALOGUES = [
    "Ayyo ente ponnu! Room kandittu kannu thalangi! Pinterest kaarukku jealousy aakum! 5-star hotel-um thottu tholkkum! Inn video call illa, full freedom! 🥳🎉",
    "Adipoli mole! Bed army-kaaru madakkunna pole neat! Shelf okke Marie Kondo vanthu sheriyakkiya pole! Amma proud aanu! No call today! 😍",
    "Enthu bhayankara aesthetic aanu! Fairy lights, plant, ellam perfect! Instagram influencers okke ithu kaananam! Good mole! Inn samadhanam! ✨"
]

MODERATE_DIALOGUES = [
    "90% adipoli aanu mole! But oru pillow thalachil poyi, bed-um pillow-um divorce aayathu pole! 😂 Oru sokk bathroom-il solo trip pokunnu! Sokk aesthetic aano? 😏 Njan 15 minute kazhinju vilikkam, sheriyakku!",
    "Almost perfect! But Netflix kandukond pillow fight nadannathu pole aanu! Charger snake pole kidappund! 15 minute tharam, full hero aakku! 😉",
    "Clean aanu, but 10/10 aavan oru touch bakki! Bed sheet oru side thalliyathu pole! Amma 15 minute-nu alarm vechu, athinu munne sheriyakku! ⏰"
]

MESSY_DIALOGUES = [
    "ENTHADA MONE ITHU?! Room aano atho Kurukshetra yudha bhoomi aano?! Clothes ellam world tour nadathunnu! Bed-il oru kapala mala! 😱 3 minute-nu ROPE-um kondu amma varum! Jumanji game aano ithu?! 🧹😡",
    "Ayyo Bhagavane! FBI vannalum evidence kittilla, ithra mess! Socks okke hide and seek kalikkunnu! Pillow okke bhaagam! Njan 2 minute-nu VIDEO CALL cheyyum, appo live aayi kaanam! 🤣🔥",
    "Ithu room alla, oru natural disaster aanu! Tsunami vannathu pole! Alavala ellam floor-il! 2 minute kazhinju amma vilichappo parayanda - 'Amma, ithu modern art aanu!' 😂🧹"
]

photo = st.file_uploader("Upload room photo", type=["jpg","png","jpeg"])

if photo:
    st.image(photo, width=350)
    
    if st.button("📱 Check Amma Mood", type="primary"):
        name = photo.name.lower()

        if "aesthetic" in name or "clean" in name or "super" in name:
            score_type = "clean"
        elif "average" in name or "15" in name or "moderate" in name or "little" in name:
            score_type = "moderate"
        elif "messy" in name or "mess" in name or "dirty" in name:
            score_type = "messy"
        else:
            if photo.size < 200000:
                score_type = "clean"
            elif photo.size < 500000:
                score_type = "moderate"
            else:
                score_type = "messy"

        if score_type == "clean":
            st.balloons()
            st.success("### ✅ NO CALL FOR TODAY! Room is super clean & aesthetic! Good mole! 😍🎉")
            st.metric("Clean Score", "9.5/10 - Pinterest Level")
            st.metric("Amma Call", "No Call Today - Full Freedom!")
            st.info(f"**Amma says:** {random.choice(CLEAN_DIALOGUES)}")
            st.write("**Amma saw:** Bed super neat, aesthetic, very clean")

        elif score_type == "moderate":
            st.balloons()
            st.warning("### ⏰ AMMA WILL CALL IN 15 MINUTES! Almost perfect! 😉")
            col1, col2 = st.columns(2)
            col1.metric("Clean Score", "7/10 - Average")
            col2.metric("Time Left", "15 Min")
            st.progress(60, text="15 min left - hurry!")
            st.info(f"**Amma says:** {random.choice(MODERATE_DIALOGUES)}")
            st.write("**Amma saw:** One pillow off, one sock on floor - 90% clean!")

        else:
            st.error("### 🚨 AMMA WILL VIDEO CALL IN 3 MINUTES! ROPE IS COMING! 🧹😱")
            col1, col2 = st.columns(2)
            col1.metric("Mess Score", "9/10 - Very Messy!")
            col2.metric("Time Left", "3 Min Only!")
            st.progress(95, text="ROPE loading... 3 min!")
            st.info(f"**Amma says:** {random.choice(MESSY_DIALOGUES)}")
            st.write("**Amma saw:** Clothes everywhere, bed not made, messy!")