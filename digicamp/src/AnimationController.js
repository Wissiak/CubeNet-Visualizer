import React from "react";
import "./AnimationController.css";


function AnimationControls({setStep, currentStep}) {

  const numberOfSteps = 6

  function nextStep() {
    setStep(Math.min(currentStep + 1, numberOfSteps));
  }

  function prevStep() {
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
