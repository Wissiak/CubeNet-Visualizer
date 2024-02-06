import React, { useState } from "react";
import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import hamburger from "./assets/burger-menu.svg";
import "./Navigation.css";

function Navigation() {
  const [collapsed, setCollapsed] = useState(true);
  function Toggle() {
    const [isToggled, setIsToggled] = useState(false);

    const toggle = () => {
      setIsToggled(!isToggled);
    };

    return (
      <div className={`toggle-container${isToggled ? ' toggled' : ''}`} onClick={toggle}>
        <div className={`toggle-button ${isToggled ? 'toggled' : ''}`}></div>
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
      />
      <Sidebar collapsed={collapsed} collapsedWidth={0} style={{ height: "100vh" }} width={`${sidebarWidth}px`}>
        <Menu>
          <div className="toggle-sides-container">
            <label className="toggle-sides-label">Enable Highlighting</label><Toggle></Toggle>
          </div>
          <SubMenu label="Cube Nets">
            <MenuItem> Net1 </MenuItem>
            <MenuItem> Net2 </MenuItem>
            <MenuItem> Net3 </MenuItem>
            <MenuItem> Net4 </MenuItem>
            <MenuItem> Net5 </MenuItem>
            <MenuItem> Net6 </MenuItem>
            <MenuItem> Net7 </MenuItem>
            <MenuItem> Net8 </MenuItem>
            <MenuItem> Net9 </MenuItem>
            <MenuItem> Net10 </MenuItem>
            <MenuItem> Net11 </MenuItem>
          </SubMenu>
        </Menu>
      </Sidebar>
    </span>
  );
}
export default Navigation;
