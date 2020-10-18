import React, { Component } from 'react';
import { Button, Card, Collapse, Popconfirm, message, Alert, Tooltip } from 'antd';
import { PlayCircleOutlined, CameraOutlined, DislikeOutlined, LikeOutlined, InfoCircleOutlined } from '@ant-design/icons';
import './Display.css';

const { Panel } = Collapse;

function confirm(e) {
    console.log(e);
    message.success('Click no Sim');
}

function cancel(e) {
    console.log(e);
    message.error('Click on Não');
}


class Display extends Component {



    render() {
        function dif(value){
            if(value< 3){
                return "easy"
            }
            else if(value< 7){
                return "medium"
            }
            else{
                return "hard"
            }
        }

        let displayContent
        let moreInfo
        let definition
        let feedback
        let tooltipText
        if(this.props.content != null) {
            if (this.props.content.definition[0] === "Não foram encontrados resultados."){
                displayContent = <div><Alert
                message="Erro!"
                description="Não foram encontrados resultados."
                type="error"
                showIcon
            /></div>
            }else{

                tooltipText = <span>
                    Índice de legibilidade
                    <p>1-3 Fácil</p>
                    <p>3-7 Médio</p>
                    <p>&gt;7 Dificil</p>
                    </span>

                feedback =
                    <div id="feedback">
                        <Button type="link"><LikeOutlined /></Button>
                        <Popconfirm
                        title="Deseja uma nova explicação?"
                        onConfirm={confirm}
                        onCancel={cancel}
                        okText="Sim"
                        cancelText="Não"
                    >
                            <Button type="link"><DislikeOutlined /></Button>
                        </Popconfirm>
                    </div>


                    moreInfo = this.props.content.additionalInfo.map((item, index) => (
                        <p><a href={item} key={index}>{item}</a></p>
                    ));


                definition = this.props.content.definition.map((item, index) => (
                    <div id={index}>
                        <Card title={`${index+1}. ${this.props.content.expression}`} style={{ width: '90%' }}>
                            <p>{Object.keys(item)[0]}  &nbsp; <a href={`https://www.google.com/search?q=${item[0]}&tbm=isch`} target="_blank" rel="noopener noreferrer"><CameraOutlined style={{ fontSize: '30 px'}} /></a></p>
                            <p>
                                <Button type="primary">Visualizar<PlayCircleOutlined /></Button>

                                <div id="score"> Índice: &nbsp;
                                <span difficulty={dif(Object.values(item)[0])}>{Object.values(item)[0]}</span> &nbsp;
                                <Tooltip placement="bottomLeft" title={tooltipText}><InfoCircleOutlined /></Tooltip>
                            </div>
                            {feedback}
                        </p>
                    </Card>
                    <br />
                </div>
                ));


                displayContent =
                    <div>
                        {definition}
                        <Collapse defaultActiveKey={['1','2']} style={{ width: '90%' }}>
                            <Panel header="Fontes" key="1">
                                <p><a href={this.props.content.source}>{this.props.content.source}</a></p>
                            </Panel>
                            <Panel header="Informação Adicional" key="2">
                                {moreInfo}
                            </Panel>
                        </Collapse>
                    </div>
            }
        }else{
            displayContent = ""
        }

        return (
            <div className="Display">
                { displayContent }
            </div>
        )
    }
}

export default Display;
