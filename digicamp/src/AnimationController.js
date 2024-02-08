import React, { useEffect } from 'react';
import "./AnimationController.css";

function AnimationControls({ setStep, currentStep, onStepChange }) {
  const numberOfSteps = 6;

  function nextStep() {
    onStepChange(currentStep, currentStep + 1);
    setStep(Math.min(currentStep + 1, numberOfSteps));
  }

  function prevStep() {
    onStepChange(currentStep, currentStep - 1);
    setStep(Math.max(currentStep - 1, 1));
  }

  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key === 'ArrowRight') {
        nextStep();
      }else if(event.key === 'ArrowLeft'){
        prevStep();
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => {
        document.removeEventListener('keydown', handleKeyDown);
    };
  }, [currentStep, prevStep, nextStep]);

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
