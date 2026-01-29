# NOSTR - Notes and Other Stuff Transmitted by *Relays*


## O que é?

Se trata de um protocolo de comunicação tal como TCP-IP e HTTP desenvolvido para ser resistente à censura.

O protocolo tem como base a utilização de **eventos** que são transmitidos como *JSON* de forma simples e flexivel. utilizando criptografia de chaves públicas para as próprias chaves e assinaturas. Isso torna a criação e expansão de novos *relays* e clientes simples e prática.

Outro fator importante é não depender de servidores especificos e limitados. *Relays* têm desde sua criação o pressuposto de que desaparecerão em algum momento e são construídos de forma que sua ausência seja rapidamente suprida por outro *relay*.

"Uma vez que as contas do Nostr são baseadas em criptografia de chave pública, é fácil verificar que as mensagens foram realmente enviadas pelo utilizador em questão." [^1]



## Estrutura

O funcionamento do protocolo **NOSTR** como já mencionado pode ser definido em *clientes* e *relays*.

### Clientes
 São os meios que tornam possiveis a leitura e escrita de informações nos *relays*. 
 Exemplos: Aplicações móveis/web de redes sociais.

 O fato do protocolo ter uma implementação simples e flexível facilita a exploração das capacidadades dessa tecnologia em diferentes aspectos da internet. Há casos de foco em desenvolvimento de UI, pagamentos via *lightning* ou até mesmo jogos de xadrez. [^2]

 Além disso, o usuário pode trocar de "cliente" sem muitas preocupações, já que o cliente é apenas o meio de acesso. Desde que o cliente utilizado esteja "olhando" para o mesmo conjunto de *relays*, as informações e mensagens mostradas serão as mesmas em todos os clientes.

 Por questões de segurança, é recomendado não disponibilizar sua chave privada no cliente. importante notar que nesse protocolo, sua chave privada é quase literalmente sua identidade, caso seja comprometida ou vazada por meio de *bugs* ou brechas, a unica solução seria começar tudo do zero, construindo sua identidade do início.

#### Alguns clientes conhecidos:

##### Web
- [Iris](https://iris.to/?utm_source=nostr.how&ref=nostr.how)
- [Snort](https://snort.social/?utm_source=nostr.how&ref=nostr.how)
- [Coracle](https://coracle.social/?utm_source=nostr.how&ref=nostr.how)
- [Nostrudel](https://nostrudel.ninja/?utm_source=nostr.how&ref=nostr.how)
- [Primal](https://primal.net/?utm_source=nostr.how&ref=nostr.how)


##### Desktop
- [Gossip](https://www.github.com/mikedilger/gossip)
- [Nostur](https://www.nostur.com/)
##### IOS
- [Damus](https://apps.apple.com/app/damus/id1628663131)
- [Nostur](https://www.nostur.com/)
- [Nootti](https://www.nootti.com/)
##### Android
- [Amethyst](https://play.google.com/store/apps/details?id=com.vitorpamplona.amethyst)




 ### *Relays*
São bases de dados com funcionalidades extras. Permitem que os clientes tenham acesso as informações neles armazenadas.

São como os servidores *backend* do NOSTR, permitem os clientes mandarem as mensagens, podendo ou não armazena-las e transmiti-las para outros clientes.

Importante notar que, ao utilizar um cliente nostr e ele aparentar estar lento e com pouca responsividade, muito provavelmente o culpado seja o conjunto de *relays* utilizados, sendo valido adicionar mais alguns, ou até mesmo retirando outros.

A maioria dos *relays* atualmente não requerem pagamento para utilização, porém é esperado que a norma para o futuro seja *relays* pagos.

Aqui está uma [lista](https://relay.exchange/) dos *relays* atualmente pagos e quanto custam, assim como quem os opera.

Já essa é uma [lista](https://legacy.nostr.watch/relays/find) com possivelmente todos os *relays* disponiveis.

#### Se todos os *relays* que uso pararem de funcionar?

Caso ocorra de todos os *relays* utilizados acabarem ficando *offline* ou removidos, as informações guardadas neles não podem ser recuperadas. Esse é um dos motivos pelos quais o protocolo *nostr* busca garantir a utilização de tantos *relays*, para que o conceito e utilização de *backups* seja utilizado ao seu máximo.








# Referências
[^1]: [nostr.how](https://nostr.how/pt/what-is-nostr)
[^2]: [jester](https://jesterui.github.io/?utm_source=nostr.how&ref=nostr.how)