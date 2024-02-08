import "./App.css";
import React, { useRef, useState, useEffect } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { useLoader } from "@react-three/fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { OrbitControls, PerspectiveCamera } from "@react-three/drei";
import { AnimationControls } from "./AnimationController.js";
import ar from "./assets/ar-symbol.svg";
import * as THREE from "three";
import NetHelper from "./NetHelper.js";

let currentTime = 0

const Directions = {
  Forward: "forward",
  Backward: "backward",
}

function Scene({ config, step, direction, shouldPlayAnim = true, backgroundTexture }) {
  const [isPlaying, setIsPlaying] = useState(true);

  useEffect(() => {
    if (shouldPlayAnim) {
      setIsPlaying(true);
    }
  }, [step]);

  const netPath = `/nets/net_${String(config.net).padStart(2, '0')}/`;
  const gltf = useLoader(GLTFLoader, netPath + "net.glb");
  const grid = useLoader(GLTFLoader, netPath + "grid.glb");

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
    setIsPlaying(false)
    if (shouldPlayAnim) {
      switch (direction) {
        case Directions.Forward:
          if (mixer?.time + delta < step - 1) {
            mixer?.update(delta);
            setIsPlaying(true);
          } else {
            mixer?.setTime(step - 1);
          }
          currentTime = mixer?.time;
          break;
        case Directions.Backward:
          if (mixer?.time - delta * 2 > step - 1) {
            mixer?.update(-delta * 2);
            setIsPlaying(true);
          } else {
            mixer?.setTime(step - 1);
          }
          currentTime = mixer?.time;
          break;
      }
    } else {
      mixer?.setTime(step - 1);
    }
  })

  return (
    <>
      <group dispose={null}>
        <primitive object={gltf.scene} />
        <primitive object={grid.scene} />
        {config.enableHighlight && !isPlaying ? <NetHelper netPath={netPath} step={step} active /> : <></>}
      </group>
    </>
  );
}

function App({ config }) {
  const [currentStep, setStep] = useState(1);
  const [direction, setDirection] = useState(Directions.Forward);
  const [cameraEnabled, setCameraEnabled] = useState(false);
  const videoRef = useRef(null);
  const cameraRef = useRef();

  function changeDirection(old, next) {
    setDirection(old < next ? Directions.Forward : Directions.Backward);
  }

  useEffect(() => {
    setStep(1);
    setDirection(Directions.Forward);
  }, [config.net]);

  const toggleCameraFeed = async () => {
    if (cameraEnabled) {
      const tracks = videoRef.current.srcObject.getTracks();
      tracks.forEach(track => track.stop());
      videoRef.current.srcObject = null;
      setCameraEnabled(false);
    } else {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ video: true });
          if (videoRef.current) {
            videoRef.current.srcObject = stream;
            setCameraEnabled(true);
          }
        } catch (err) {
          console.error("An error occurred: " + err);
        }
      }
    }
  };

  const videoBackgroundStyle = cameraEnabled ? {} : { backgroundColor: 'white' };

  return (
    <>
      <video playsInline autoPlay muted ref={videoRef} className="bg-video" style={videoBackgroundStyle} />
      <img src={ar} width={45} className="ar-symbol" onClick={toggleCameraFeed} />
      <Canvas style={{ width: "100%", height: "100%" }}>
        <OrbitControls makeDefault
          target={[0, 0.5, 0]}
          maxPolarAngle={Math.PI / 2 - 0.05}
          minDistance={1.5}
          maxDistance={40}
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
        <Scene step={currentStep} direction={direction} shouldPlayAnim={!config.skipAnim} config={config} />
        <pointLight position={[-10, -10, -10]} decay={0} intensity={Math.PI} />
      </Canvas>

      <AnimationControls setStep={setStep} currentStep={currentStep} onStepChange={changeDirection} />
    </>
  );
}

export default App;
