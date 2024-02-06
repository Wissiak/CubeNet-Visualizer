import React, { useState } from "react";
import { Sidebar, Menu, MenuItem, SubMenu } from "react-pro-sidebar";
import hamburger from "./assets/burger-menu.svg";
import "./Navigation.css";

function Navigation() {
  const [collapsed, setCollapsed] = useState(true);
  const sidebarWidth = 200;
  return (
    <span>
      <img
        src={hamburger}
        width={40}
        style={{ left: collapsed ? 10 : sidebarWidth + 10}}
        className="hamburger"
        onClick={() => setCollapsed(!collapsed)}
      />
      <Sidebar collapsed={collapsed} collapsedWidth={0} style={{ height: "100vh" }} width={`${sidebarWidth}px`}>
        <Menu>
          <SubMenu label="Charts">
            <MenuItem> Pie charts </MenuItem>
            <MenuItem> Line charts </MenuItem>
          </SubMenu>
          <MenuItem> Documentation </MenuItem>
          <MenuItem> Calendar </MenuItem>
        </Menu>
      </Sidebar>
    </span>
  );
}
export default Navigation;
