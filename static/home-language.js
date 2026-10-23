(() => {
  "use strict";

  const translations = {
    zh: {
      title: "首页｜未来职业探索",
      description: "从技能、经验和兴趣出发，慢慢找到适合你的未来职业。",
      toggleLabel: "切换到英文",
      brand: "未来职业探索",
      homeAria: "未来职业探索首页",
      welcomeEyebrow: "送给正在思考下一步的你",
      welcomeTitleLead: "欢迎你，",
      welcomeTitleMain: "慢慢找到自己的方向",
      welcomeTitlePunctuation: "。",
      welcomeCopyFirst: "这里没有标准答案，也不必急着决定。",
      welcomeCopySecond: "带上你的兴趣、经验与技能，我们陪你一起，把未来看得清晰一点。",
      welcomeEnter: "好，我们慢慢开始",
      welcomeReassurance: "也可以停留片刻，页面会为你慢慢展开",
      headerNote: "给下一段旅程一点空间",
      heroEyebrowOne: "技能",
      heroEyebrowTwo: "经验",
      heroEyebrowThree: "兴趣",
      heroTitleLead: "探索适合你的",
      heroTitleAccent: "未来职业",
      heroTitlePunctuation: "。",
      heroCta: "陪我一起，慢慢找方向",
      heroIntroFirst: "告诉我们你掌握的技能、相关经验和兴趣方向，",
      heroIntroSecond: "查看职业匹配结果、技能差距和学习建议。",
      heroReassurance: "没有标准答案，只从你出发",
      illustrationAria: "抽象的职业探索路径插画",
      artStart: "从此刻出发",
      artPace: "你的节奏",
      artDestination: "新的可能",
      artDestinationNote: "慢慢找到方向",
      artCaption: "每一种经历，都能成为下一步的线索",
      scrollAria: "向下浏览",
      scrollLabel: "向下探索",
      pathwayEyebrow: "一段温和的探索",
      pathwayHeading: "把模糊的想法，变成清晰的下一步。",
      pathwayNote: "从认识自己开始，不必一次想清所有答案。",
      pathwayOneTitle: "了解你的优势",
      pathwayOneDescription: "根据你填写的技能、经验和兴趣，计算职业匹配度。",
      pathwayOneTag: "优势画像",
      pathwayOneAria: "了解你的优势，陪我一起探索下一步",
      pathwayTwoTitle: "发现技能差距",
      pathwayTwoDescription: "查看目标职业需要哪些技能，以及你可以继续学习什么。",
      pathwayTwoTag: "成长地图",
      pathwayTwoAria: "发现技能差距，陪我一起探索下一步",
      pathwayThreeTitle: "规划下一步",
      pathwayThreeDescription: "查看职业学习步骤及其关联的可持续发展目标。",
      pathwayThreeTag: "行动建议",
      pathwayThreeAria: "规划下一步，陪我一起探索下一步",
      footerCopy: "你的下一步，不需要和任何人一样。",
      footerCta: "陪我继续探索"
    },
    en: {
      title: "Home | Career Explorer",
      description: "Explore careers through your skills, experience, and interests—and find a next step that feels right for you.",
      toggleLabel: "Switch to Chinese",
      brand: "Career Explorer",
      homeAria: "Career Explorer home",
      welcomeEyebrow: "For anyone thinking about what comes next",
      welcomeTitleLead: "Welcome.",
      welcomeTitleMain: "Find your direction, at your own pace",
      welcomeTitlePunctuation: "",
      welcomeCopyFirst: "There is no single right answer, and nothing to rush.",
      welcomeCopySecond: "Bring your interests, experience, and skills. We’ll help you see a little more clearly what could come next.",
      welcomeEnter: "Let’s take the first step",
      welcomeReassurance: "Stay a moment if you like. The page will gently unfold.",
      headerNote: "Make room for what comes next",
      heroEyebrowOne: "Skills",
      heroEyebrowTwo: "Experience",
      heroEyebrowThree: "Interests",
      heroTitleLead: "Explore work that",
      heroTitleAccent: "fits who you are",
      heroTitlePunctuation: ".",
      heroCta: "Help me find my direction",
      heroIntroFirst: "Share your skills, experience, and interests",
      heroIntroSecond: "to see career matches, skill gaps, and learning ideas.",
      heroReassurance: "No perfect answers. Start with you.",
      illustrationAria: "An abstract illustration of a career exploration path",
      artStart: "Start where you are",
      artPace: "Your own pace",
      artDestination: "New possibilities",
      artDestinationNote: "Find your direction",
      artCaption: "Every experience can point to what comes next",
      scrollAria: "Browse further down",
      scrollLabel: "Explore below",
      pathwayEyebrow: "A gentler kind of exploration",
      pathwayHeading: "Turn a vague idea into a clear next step.",
      pathwayNote: "Start by getting to know yourself. No need to solve it all today.",
      pathwayOneTitle: "See your strengths",
      pathwayOneDescription: "Explore career matches based on the skills, experience, and interests you share.",
      pathwayOneTag: "Your strengths",
      pathwayOneAria: "See your strengths and explore a next step with me",
      pathwayTwoTitle: "Spot skill gaps",
      pathwayTwoDescription: "See which skills a career calls for, and what you could learn next.",
      pathwayTwoTag: "Room to grow",
      pathwayTwoAria: "Spot skill gaps and explore a next step with me",
      pathwayThreeTitle: "Plan what comes next",
      pathwayThreeDescription: "Explore learning steps for a career and the sustainable development goals they connect to.",
      pathwayThreeTag: "Next steps",
      pathwayThreeAria: "Plan what comes next and explore a next step with me",
      footerCopy: "Your next step doesn’t have to look like anyone else’s.",
      footerCta: "Keep exploring with me"
    }
  };

  const root = document.documentElement;
  const welcome = document.getElementById("welcome");
  const enterButton = document.getElementById("enter-home");
  const sections = [...document.querySelector("main").children].filter((element) => element !== welcome);
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let leaving = false;
  let welcomeTimer;

  function readPreference() {
    try {
      const saved = window.localStorage.getItem("career-home-language");
      return saved === "en" || saved === "zh" ? saved : "zh";
    } catch (_) {
      return "zh";
    }
  }

  function savePreference(language) {
    try {
      window.localStorage.setItem("career-home-language", language);
    } catch (_) {
      // Storage can be unavailable in private browsing or restricted contexts.
    }
  }

  function applyLanguage(language) {
    const selected = language === "en" ? "en" : "zh";
    const copy = translations[selected];
    root.lang = selected === "en" ? "en" : "zh-CN";
    document.title = copy.title;
    const description = document.querySelector('meta[name="description"]');
    if (description) description.setAttribute("content", copy.description);

    document.querySelectorAll("[data-i18n]").forEach((element) => {
      const value = copy[element.dataset.i18n];
      if (value !== undefined) element.textContent = value;
    });
    document.querySelectorAll("[data-i18n-aria-label]").forEach((element) => {
      const value = copy[element.dataset.i18nAriaLabel];
      if (value !== undefined) element.setAttribute("aria-label", value);
    });

    document.querySelectorAll("[data-language-toggle]").forEach((button) => {
      button.textContent = selected === "zh" ? "English" : "中文";
      button.setAttribute("aria-label", copy.toggleLabel);
      button.setAttribute("lang", selected === "zh" ? "en" : "zh-CN");
    });
    savePreference(selected);
  }

  const initialLanguage = readPreference();
  applyLanguage(initialLanguage);

  document.querySelectorAll("[data-language-toggle]").forEach((button) => {
    button.addEventListener("click", () => {
      if (button.classList.contains("welcome-language-toggle")) {
        window.clearTimeout(welcomeTimer);
      }
      applyLanguage(root.lang === "en" ? "zh" : "en");
    });
  });

  sections.forEach((element) => {
    element.inert = true;
  });

  let welcomeFocusables = [...welcome.querySelectorAll('button:not([disabled]), a[href], [tabindex]:not([tabindex="-1"])')];
  enterButton.focus({ preventScroll: true });

  function enterHome() {
    if (leaving) return;
    leaving = true;
    window.clearTimeout(welcomeTimer);
    welcome.classList.add("is-leaving");
    window.setTimeout(() => {
      const restoreFocus = welcome.contains(document.activeElement);
      welcome.remove();
      sections.forEach((element) => {
        element.inert = false;
      });
      if (restoreFocus) {
        const title = document.querySelector(".hero-copy h1");
        title.tabIndex = -1;
        title.focus({ preventScroll: true });
      }
    }, reduceMotion ? 0 : 760);
  }

  enterButton.addEventListener("click", enterHome);
  welcome.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      event.preventDefault();
      enterHome();
      return;
    }
    if (event.key === "Tab") {
      welcomeFocusables = [...welcome.querySelectorAll('button:not([disabled]), a[href], [tabindex]:not([tabindex="-1"])')];
      const first = welcomeFocusables[0];
      const last = welcomeFocusables[welcomeFocusables.length - 1];
      if (event.shiftKey && (document.activeElement === first || !welcome.contains(document.activeElement))) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && (document.activeElement === last || !welcome.contains(document.activeElement))) {
        event.preventDefault();
        first.focus();
      }
    }
  });

  welcomeTimer = window.setTimeout(enterHome, reduceMotion ? 1400 : 6400);
})();
