import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# ===== 한글 폰트 설정 =====
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# ===== 그래프 =====
st.subheader("📈 가격 변화")

fig, ax = plt.subplots(figsize=(5, 2.8))  # 작고 가독성 있게

for name in ITEMS:
    history = st.session_state.stocks[name]["history"]
    days = list(range(1, len(history) + 1))  # Day 1,2,3...
    ax.plot(
        days,
        history,
        marker="o",
        linewidth=2,
        label=name
    )

ax.set_xlabel("Day")
ax.set_ylabel("가격(원)")
ax.grid(alpha=0.3)

# 범례를 아래로
ax.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.25),
    ncol=3,
    fontsize=8
)

st.pyplot(fig)
