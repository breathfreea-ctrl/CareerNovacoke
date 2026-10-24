(() => {
  const screen = document.getElementById("entry-screen");
  const continueButton = document.getElementById("entry-continue");
  const welcomeCard = document.querySelector(".welcome-card");
  const header = document.querySelector(".site-header");
  const footer = document.querySelector(".site-footer");

  if (!screen || !continueButton || !welcomeCard) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  screen.hidden = false;
  welcomeCard.inert = true;
  if (header) header.inert = true;
  if (footer) footer.inert = true;
  continueButton.focus({ preventScroll: true });

  let dismissed = false;
  let finished = false;
  let exitTimer;
  const finishDismiss = () => {
    if (finished) return;
    finished = true;
    window.clearTimeout(exitTimer);
    screen.hidden = true;
    welcomeCard.inert = false;
    if (header) header.inert = false;
    if (footer) footer.inert = false;
    document.querySelector(".welcome-card .button--primary")?.focus({ preventScroll: true });
  };

  const dismiss = () => {
    if (dismissed) return;
    dismissed = true;
    window.clearTimeout(dismissTimer);
    continueButton.disabled = true;
    screen.classList.add("is-leaving");
    document.removeEventListener("keydown", onKeydown);
    screen.addEventListener("transitionend", finishDismiss, { once: true });
    exitTimer = window.setTimeout(finishDismiss, 300);
  };

  const onKeydown = (event) => {
    if (event.key === "Tab") {
      event.preventDefault();
      continueButton.focus({ preventScroll: true });
      return;
    }
    if (event.key === "Escape" || event.key === "Enter") {
      event.preventDefault();
      dismiss();
    }
  };

  const dismissTimer = window.setTimeout(dismiss, 2100);
  continueButton.addEventListener("click", dismiss);
  document.addEventListener("keydown", onKeydown);
})();
