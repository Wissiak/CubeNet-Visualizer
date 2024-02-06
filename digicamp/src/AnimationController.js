import React, { useState} from "react";
import "./AnimationController.css";

function AnimationControls() {
  const numberOfSteps = 5;
  const [currentStep, setStep] = useState(1);

  function nextStep() {
    setStep(currentStep + 1);
  }

  function prevStep() {
    setStep(currentStep - 1);
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

export default AnimationControls;
