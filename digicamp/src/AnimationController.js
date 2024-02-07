import React from "react";
import "./AnimationController.css";

let lastAction = new Date().getTime() - 1000; 

function AnimationControls({ setStep, currentStep, onStepChange, config }) {
  const numberOfSteps = 6;

  function nextStep() {
    const now = new Date().getTime();
    if (now - lastAction < 1000) {
      // wait until animation is over to not skip any steps
      return;
    }
    onStepChange(currentStep, currentStep + 1);
    setStep(Math.min(currentStep + 1, numberOfSteps));
    lastAction = now;
  }

  function prevStep() {
    const now = new Date().getTime();
    if (!config.skipReverseAnim && now - lastAction < 1000) {
      // wait until animation is over to not skip any steps
      return;
    }
    onStepChange(currentStep, currentStep - 1);
    setStep(Math.max(currentStep - 1, 1));
    lastAction = now;
  }

  return (
    <div className="animation-control">
      <img
        className="chevron"
        src="chevron-left.webp"
        alt="Previous"
        id="control-prev"
        disabled={currentStep <= 1}
        onClick={prevStep}
      />
      <p id="control-status">
        {currentStep}&nbsp;/&nbsp;{numberOfSteps}
      </p>
      <img
        className="chevron"
        src="chevron-right.webp"
        alt="Next"
        id="control-next"
        disabled={currentStep >= numberOfSteps}
        onClick={nextStep}
      />
    </div>
  );
}

export { AnimationControls };
