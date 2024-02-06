import React, { useState } from "react";
import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import hamburger from "./assets/burger-menu.svg";
import "./Navigation.css";

function activateCubeNet(netNumber) {
  console.log("Activating net number " + netNumber);
}

function Navigation() {
  const [collapsed, setCollapsed] = useState(true);
  function Toggle() {
    const [isToggled, setIsToggled] = useState(false);

    const toggle = () => {
      setIsToggled(!isToggled);
    };

    return (
      <div
        className={`toggle-container${isToggled ? " toggled" : ""}`}
        onClick={toggle}
      >
        <div className={`toggle-button ${isToggled ? "toggled" : ""}`}></div>
      </div>
    );
  }
  const sidebarWidth = 250;
  return (
    <span>
      <img
        src={hamburger}
        width={40}
        style={{ left: collapsed ? 10 : sidebarWidth + 10 }}
        className="hamburger"
        onClick={() => setCollapsed(!collapsed)}
        alt="hamburger menu icon"
      />
      <Sidebar
        collapsed={collapsed}
        collapsedWidth={0}
        style={{ height: "100vh" }}
        width={`${sidebarWidth}px`}
      >
        <Menu>
          <div className="toggle-sides-container">
            <label className="toggle-sides-label">Enable Highlighting</label>
            <Toggle></Toggle>
          </div>
          <SubMenu label="Cube Nets">
            <MenuItem> Net 1 </MenuItem>
            <img
              src="nets/1.png"
              className="cube-net"
              alt="cube net nr 1"
              onClick={() => activateCubeNet(1)}
            ></img>
            <MenuItem> Net 2 </MenuItem>
            <img
              src="nets/2.png"
              className="cube-net"
              alt="cube net nr 2"
              onClick={() => activateCubeNet(2)}
            ></img>
            <MenuItem> Net 3 </MenuItem>
            <img
              src="nets/3.png"
              className="cube-net"
              alt="cube net nr 3"
              onClick={() => activateCubeNet(3)}
            ></img>
            <MenuItem> Net 4 </MenuItem>
            <img
              src="nets/4.png"
              className="cube-net"
              alt="cube net nr 4"
              onClick={() => activateCubeNet(4)}
            ></img>
            <MenuItem> Net 5 </MenuItem>
            <img
              src="nets/5.png"
              className="cube-net"
              alt="cube net nr 5"
              onClick={() => activateCubeNet(5)}
            ></img>
            <MenuItem> Net 6 </MenuItem>
            <img
              src="nets/6.png"
              className="cube-net"
              alt="cube net nr 6"
              onClick={() => activateCubeNet(6)}
            ></img>
            <MenuItem> Net 7 </MenuItem>
            <img
              src="nets/7.png"
              className="cube-net"
              alt="cube net nr 7"
              onClick={() => activateCubeNet(7)}
            ></img>
            <MenuItem> Net 8 </MenuItem>
            <img
              src="nets/8.png"
              className="cube-net"
              alt="cube net nr 8"
              onClick={() => activateCubeNet(8)}
            ></img>
            <MenuItem> Net 9 </MenuItem>
            <img
              src="nets/9.png"
              className="cube-net"
              alt="cube net nr 9"
              onClick={() => activateCubeNet(9)}
            ></img>
            <MenuItem> Net 10 </MenuItem>
            <img
              src="nets/10.png"
              className="cube-net"
              alt="cube net nr 10"
              onClick={() => activateCubeNet(10)}
            ></img>
            <MenuItem> Net 11 </MenuItem>
            <img
              src="nets/11.png"
              className="cube-net"
              alt="cube net nr 11"
              onClick={() => activateCubeNet(11)}
            ></img>
          </SubMenu>
        </Menu>
      </Sidebar>
    </span>
  );
}
export default Navigation;
