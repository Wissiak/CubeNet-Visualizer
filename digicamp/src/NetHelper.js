import React from "react";
import { useLoader } from "@react-three/fiber";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";

function NetHelper({ netPath, step }) {
    const arrows = []
    arrows.push(useLoader(GLTFLoader, netPath + "step_1_arrow.glb"))
    arrows.push(useLoader(GLTFLoader, netPath + "step_2_arrow.glb"))
    arrows.push(useLoader(GLTFLoader, netPath + "step_3_arrow.glb"))
    arrows.push(useLoader(GLTFLoader, netPath + "step_4_arrow.glb"))
    arrows.push(useLoader(GLTFLoader, netPath + "step_5_arrow.glb"))
    arrows.push(useLoader(GLTFLoader, netPath + "step_6_arrow.glb"))

    return (
        <>
            <primitive object={arrows[step-1].scene} />
        </>
    )
}

export default NetHelper;
