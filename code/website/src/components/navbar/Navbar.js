import React, { Component } from 'react';
import { Menu, Dropdown } from 'antd';
import 'antd/dist/antd.css';
import '../app/App.css';


const menu = (
    <Menu>
    <Menu.Item>
    <a target="_blank" rel="noopener noreferrer">
    Português
    </a>
    </Menu.Item>
    </Menu>
);

class Navbar extends Component {


    render(){
        return(
            <div className="Navbar">
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
            <Menu.Item key="1">
            <Dropdown overlay={menu}>
            <a className="ant-dropdown-link" onClick={e => e.preventDefault()}>
            Linguagem
            </a>
            </Dropdown>
            </Menu.Item>
            </Menu>
            </div>
        )
    }
}

export default Navbar;
