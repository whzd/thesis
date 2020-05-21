import React, { Component } from 'react';
import { Menu, Dropdown } from 'antd';
import './Navbar.css';
import { DownOutlined } from '@ant-design/icons';

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
            <Dropdown overlay={menu}>
            <a className="ant-dropdown-link" onClick={e => e.preventDefault()}>
                    Linguagem <DownOutlined />
            </a>
            </Dropdown>
            </div>
        )
    }
}

export default Navbar;
