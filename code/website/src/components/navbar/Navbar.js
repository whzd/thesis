import React, { Component } from 'react';
import { Menu, Dropdown } from 'antd';
import './Navbar.css';
import { DownOutlined } from '@ant-design/icons';
import FlagIcon from './FlagIcon.js';
import i18n from '../../i18next';

class Navbar extends Component {

    constructor(props){
        super(props)
        this.state = {
            lng: this.props.language
        }
        this.onLanguageChanged = this.onLanguageChanged.bind(this)
    }

    componentWillUpdate(nextprops) {
        if(nextprops.language !== this.props.language){
            this.setState({
                lng: nextprops.language
            })
        }
    }

    onLanguageChanged = ({key}) => {
        this.setState({
            lng: key
        })
        this.props.handleLanguageChange(key)
    }
    menu = (
        <Menu onClick={this.onLanguageChanged}>
            <Menu.Item key='pt'>
                <a target="_blank" rel="noopener noreferrer">
                    <FlagIcon code='pt' size='lg'/> Português
                </a>
            </Menu.Item>
            <Menu.Item key='en'>
                <a target="_blank" rel="noopener noreferrer">
                    <FlagIcon code='gb' size='lg'/> English
                </a>
            </Menu.Item>
        </Menu>
    );


    render(){
        let lng = this.state.lng
        return(
            <div className="Navbar">
                <Dropdown overlay={this.menu}>
                    <a className="ant-dropdown-link" onClick={e => e.preventDefault()}>
                        { i18n.t('navbar.language', { lng }) } <DownOutlined />
                    </a>
                </Dropdown>
            </div>
        )
    }
}

export default Navbar;
