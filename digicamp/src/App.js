import "./App.css";
import React from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { useLoader } from "@react-three/fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import { OrbitControls } from "@react-three/drei";
import * as THREE from "three";

function Scene() {
  const gltf = useLoader(GLTFLoader, "/nets/case_01.glb");

  const mixer = new THREE.AnimationMixer(gltf.scene);
  gltf.animations.forEach((clip) => {
    const action = mixer.clipAction(clip);
    action.play();
  });
  useFrame((state, delta) => {
    mixer?.update(delta)
})

  return <primitive object={gltf.scene} />;
}

function App() {
  return (
    <Canvas style={{ width: "100%", height: "100%" }}>
      <OrbitControls makeDefault />
      <ambientLight intensity={Math.PI / 2} />
      <spotLight
        position={[10, 10, 10]}
        angle={0.15}
        penumbra={1}
        decay={0}
        intensity={Math.PI}
      />
      <Scene />
      <pointLight position={[-10, -10, -10]} decay={0} intensity={Math.PI} />
    </Canvas>
  );
}

export default App;
