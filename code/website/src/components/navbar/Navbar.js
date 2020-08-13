import React, { Component } from 'react';
import { Menu, Dropdown } from 'antd';
import './Navbar.css';
import { DownOutlined } from '@ant-design/icons';
import FlagIcon from './FlagIcon.js';

const menu = (
    <Menu>
    <Menu.Item>
    <a target="_blank" rel="noopener noreferrer">
    <FlagIcon code='pt' size='lg'/> Português
    </a>
    </Menu.Item>
    <Menu.Item>
    <a target="_blank" rel="noopener noreferrer">
    <FlagIcon code='gb' size='lg'/> English
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
                    Língua <DownOutlined />
            </a>
            </Dropdown>
            </div>
        )
    }
}

export default Navbar;
