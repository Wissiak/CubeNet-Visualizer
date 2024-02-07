import React from "react";
import "./AnimationController.css";


function AnimationControls({setStep, currentStep, onStepChange}) {

  const numberOfSteps = 6

  function nextStep() {
    onStepChange(currentStep, currentStep + 1);
    setStep(Math.min(currentStep + 1, numberOfSteps));
  }

  function prevStep() {
    onStepChange(currentStep, currentStep - 1);
    setStep(Math.max(currentStep - 1,  1));
  }

  return (
    <div className="animation-control">
      <button
        id="control-prev"
        disabled={currentStep <= 1}
        onClick={prevStep}
      >Prev</button>
      <p id="control-status">{currentStep}&nbsp;/&nbsp;{numberOfSteps}</p>
      <button
        id="control-next"
        disabled={currentStep >= numberOfSteps}
        onClick={nextStep}
      >Next</button>
    </div>
  )
}

export { AnimationControls };
