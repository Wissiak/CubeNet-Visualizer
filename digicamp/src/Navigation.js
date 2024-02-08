import React, { useState, useRef, useEffect } from "react";
import { Sidebar, Menu, SubMenu } from "react-pro-sidebar";
import hamburger from "./assets/burger-menu.svg";
import "./Navigation.css";

function Navigation({ config }) {
  const [collapsed, setCollapsed] = useState(true);
  const navigationRef = useRef(null);


  function activateCubeNet(netNumber) {
    console.log("Activating net number " + netNumber);
    config.setNet(netNumber);
  }

  const sidebarWidth = 250;

  useEffect(() => {
    const handleOutsideClick = (event) => {
        if (navigationRef.current && !navigationRef.current.contains(event.target)) {
          setCollapsed(true);
        }
    };

    if (navigationRef.current) {
        document.addEventListener('click', handleOutsideClick);
    }

  }, []);

  return (
    <span ref={navigationRef}>
      <img
        src={hamburger}
        width={50}
        style={{ left: collapsed ? 16 : sidebarWidth + 16 }}
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
          <div id="titel-bar">
            <img src="./logo192.png" alt="logo"/>
            <h1>CubeNet</h1>
          </div>
          <div class="line"></div>
          <div className="toggle-sides-container">
            <label className="toggle-sides-label">Helper Arrows</label>
            <Toggle isToggled={config.enableHighlight} setIsToggled={config.setEnableHighlight} />
          </div>
          <div class="line"></div>

          <div className="toggle-sides-container">

            <label className="toggle-sides-label">No Animations</label>
            <Toggle isToggled={config.skipAnim} setIsToggled={config.setSkipAnim} />
          </div>
          <div class="line"></div>
          <SubMenu label="Cube Nets">
            <MenuItemCubeNet number={1} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={2} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={3} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={4} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={5} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={6} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={7} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={8} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={9} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={10} activateCubeNet={activateCubeNet} />
            <MenuItemCubeNet number={11} activateCubeNet={activateCubeNet} />
          </SubMenu>
          <SubMenu label="Advanced Shapes" style={{ opacity: 0.5 }}></SubMenu>
          <SubMenu label="Add" style={{ opacity: 0.5 }}></SubMenu>
          <SubMenu label="Subtract" style={{ opacity: 0.5 }}></SubMenu>
          <SubMenu label="Divide" style={{ opacity: 0.5 }}></SubMenu>
          <SubMenu label="3D Puzzle" style={{ opacity: 0.5 }}></SubMenu>
          <div class="line"></div>
        </Menu>
      </Sidebar>
    </span>
  );
}

function Toggle({ isToggled, setIsToggled }) {
  const toggle = () => {
    setIsToggled(!isToggled);
  };

  return (
    <div
      className={`toggle-container ${isToggled ? "toggled" : ""}`}
      onClick={toggle}
    >
      <div className={`toggle-button ${isToggled ? "toggled" : ""}`}></div>
    </div>
  );
}


function MenuItemCubeNet({ number, activateCubeNet }) {
  const label = number.toString();
  const src = `nets/${number}.png`;
  return (
    <li class="menuitem-cubenet">
      <span>{label}</span>
      <img
        src={src}
        className="cube-net"
        alt={`select ${label}`}
        onClick={() => activateCubeNet(number)}
      ></img>
    </li>
  );
}

export default Navigation;
