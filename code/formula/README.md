# LGP readability formula

The `LGP.py` class has the methods responsible for using the formula.

## JSON file configuration

\"CONFR\":\configuração da mão direita

\"IKVEC3R\":\posição da mão direita

\"QHANDR\":\ posição da mão direita

\"CONFL\":\ configuração da mão esquerda

\"IKVEC3L\":\ posição da mão esquerda

\"QHANDL\":\ posição da mão esquerda

\"FE\":\expressão facial

\"QHEAD\":posição cabeça

\"SPEED\":\velocidade

### Example

Por exemplo, a palavra “bom dia” tem 4 momentos e usa duas configurações de mão distintas (BR e DR) na mão direita (CONFR). A mão esquerda (CONFL) está com a configuração “nenhuma” em todos os momentos.
Só é utilizada a mão dominamte (máo direita); a posição da máo esquerda (QHANDL) é sempre a mesma (sensivelmente) porque os valores de IKVEC3L e QHANDL são sensivelmente iguais em todos os momentos.
Não estão configuradas as expressões faciais (FE).

```json
{"word":"bom dia","config":"[

{
\"CONFR\":\"BR\",
\"IKVEC3R\":\"0.4491543,1.218286,1.193019\",
\"QHANDR\":\"0.995081,0.05553876,0.0001156913,-0.08203727\",
\"CONFL\":\"nenhumaL\",
\"IKVEC3L\":\"0.6696563,1.025397,1.201924\",
\"QHANDL\":\"0.001743199,-0.1031564,0.7502564,0.6530481\",
\"FE\":\"0\",
\"QHEAD\":\"0.7071068,-0.7071068,-1.152023E-07,1.152023E-07\",
\"SPEED\":\"1\"
},

{
\"CONFR\":\"DR\",
\"IKVEC3R\":\"0.3865488,1.462756,1.194038\",
\"QHANDR\":\"-0.9215177,-0.08239853,-0.3769339,0.04401278\",
\"CONFL\":\"nenhumaL\",
\"IKVEC3L\":\"0.6696563,1.025397,1.201924\",
\"QHANDL\":\"0.001743199,-0.1031564,0.7502564,0.6530481\",
\"FE\":\"0\",
\"QHEAD\":\"0.7071068,-0.7071068,-1.152023E-07,1.152023E-07\",
\"SPEED\":\"1\"
},

{
\"CONFR\":\"DR\",
\"IKVEC3R\":\"0.1785315,1.598123,1.194991\",
\"QHANDR\":\"-0.8545178,-0.4388634,-0.08956606,0.2630148\",
\"CONFL\":\"nenhumaL\",
\"IKVEC3L\":\"0.6696563,1.025397,1.201924\",
\"QHANDL\":\"0.001743263,-0.1031564,0.7502563,0.6530479\",
\"FE\":\"0\",
\"QHEAD\":\"0.7071068,-0.7071068,-1.152023E-07,1.152023E-07\",
\"SPEED\":\"1\"
},

{
\"CONFR\":\"DR\",
\"IKVEC3R\":\"0.206801,1.000081,1.192775\",
\"QHANDR\":\"0.8727098,0.4401523,-0.1005072,0.1858557\",
\"CONFL\":\"nenhumaL\",
\"IKVEC3L\":\"0.6696563,1.025397,1.201924\",
\"QHANDL\":\"0.00174331,-0.1031564,0.7502564,0.653048\",
\"FE\":\"0\",
\"QHEAD\":\"0.7071068,-0.7071068,-1.152023E-07,1.152023E-07\",
\"SPEED\":\"1\"
}

]"}
```
