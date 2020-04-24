import React, { Component } from 'react';
import { Menu } from 'antd';

class Navbar extends Component {

    render(){
        return(
            <div className="Navbar">
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
            <Menu.Item key="1">Language</Menu.Item>
            <Menu.Item key="2">About</Menu.Item>
            </Menu>
            </div>
        )
    }
}

export default Navbar;
