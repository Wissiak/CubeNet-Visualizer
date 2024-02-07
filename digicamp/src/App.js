import "./App.css";
import React, { useRef, useState, useEffect } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { useLoader } from "@react-three/fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { OrbitControls, PerspectiveCamera } from "@react-three/drei";
import {AnimationControls} from "./AnimationController.js";
import * as THREE from "three";

let currentTime = 0

const Directions = {
  Forward: "forward",
  Backward: "backward",
}

function Scene({step, direction, shouldPlayReverseAnim = true}) {
  const gltf = useLoader(GLTFLoader, "/nets/case_01.glb");
  const grid = useLoader(GLTFLoader, "/nets/case_01_grid.glb");

  const mixer = new THREE.AnimationMixer(gltf.scene);

  gltf.animations.forEach((clip) => {
    const action = mixer.clipAction(clip);
    action.reset();
    action.setLoop(THREE.LoopOnce);
    action.clampWhenFinished = true;
    action.play();
  });

  //workaround: when the component is updated this value rests the same
  mixer?.setTime(currentTime)

  useFrame((state, delta) => {
    switch (direction) {
      case Directions.Forward:
        if (step - 1 - mixer?.time > 1) {
          // skip animation steps if difference too large
          mixer?.setTime(step - 1);
        }
        if (mixer?.time + delta < step - 1){
          mixer?.update(delta);
        } else {
          mixer?.setTime(step - 1);
        }
        currentTime = mixer?.time
        break;
      case Directions.Backward:
        if (shouldPlayReverseAnim) {
          if (mixer?.time - step + 1 > 1) {
            // skip animation steps if difference too large
            mixer?.setTime(step - 1);
          }
          if (mixer?.time - delta > step - 1){
            mixer?.update(-delta);
          } else {
            mixer?.setTime(step - 1);
          }
          currentTime = mixer?.time
        } else {
          mixer?.setTime(step - 1);
        }
        break;
    }
  })

  return (
    <>
      <primitive object={gltf.scene} />
      <primitive object={grid.scene} />
    </>
  );
}

function App({config}) {
  const [currentStep, setStep] = useState(1);
  const [direction, setDirection] = useState(Directions.Forward);
  const cameraRef = useRef();

  function changeDirection(old, next) {
      setDirection(old < next ? Directions.Forward : Directions.Backward);
  }

  return (
    <>
      <Canvas style={{ width: "100%", height: "100%" }}>
        <OrbitControls makeDefault 
            target={[0, 0.5, 0]}
          />

        <PerspectiveCamera
          ref={cameraRef}
          makeDefault
          fov={50} // Adjust the FOV to your desired value (in degrees)
          position={[0, 5, 5]} // Set the initial position of the camera higher
        />
        
        <ambientLight intensity={Math.PI / 2} />
        <spotLight
          position={[10, 10, 10]}
          angle={0.15}
          penumbra={1}
          decay={0}
          intensity={Math.PI}
        />
        <Scene step={currentStep} direction={direction} shouldPlayReverseAnim={!config.skipReverseAnim}/>
        <pointLight position={[-10, -10, -10]} decay={0} intensity={Math.PI} />
      </Canvas>

      <AnimationControls setStep={setStep} currentStep={currentStep} onStepChange={changeDirection}/>
    </>
  );
}

export default App;
