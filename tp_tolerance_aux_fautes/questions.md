# Questions - Système distribué et tolérance aux fautes

**1. Qu'est-ce qu'un système distribué ?**  
Un système distribué est un ensemble de composants autonomes (serveurs, nœuds) répartis sur un réseau qui collaborent pour fournir un service commun. L'utilisateur perçoit le tout comme un système unique. Dans ce TP, Serveur1 et Serveur2 forment un système distribué car ils offrent le même service web.

**2. Pourquoi utiliser plusieurs serveurs ?**  
Pour éviter qu'une panne d'un seul serveur interrompe le service (élimination du SPOF), répartir la charge entre plusieurs machines et assurer la continuité de service. Si Serveur1 tombe, Serveur2 continue à répondre aux requêtes.

**3. Qu'est-ce qu'un SPOF (Single Point Of Failure) ?**  
Un SPOF est un composant unique dont la défaillance entraîne l'arrêt complet du service. Dans une topologie sans redondance, un seul serveur, un seul switch ou un seul lien réseau constitue un SPOF. La redondance vise à éliminer tous les SPOFs.

**4. Pourquoi la redondance améliore la cybersécurité ?**  
La redondance renforce la résilience face aux attaques de type DoS/DDoS : si un composant est saturé ou compromis, les autres prennent le relais. Elle garantit la disponibilité (le "A" de la triade CIA : Confidentialité, Intégrité, Disponibilité), qui est un pilier fondamental de la cybersécurité.

**5. Que se passe-t-il si un switch tombe en panne ?**  
Avec la topologie de ce TP :
- Si Switch1 tombe : PC1 et Serveur1 sont isolés. PC2 et Serveur2 restent joignables via Switch2 → Routeur. Le lien Switch1-Switch2 étant coupé, Switch2 ne peut plus atteindre Serveur1.
- Si Switch2 tombe : symétrique, PC2 et Serveur2 sont isolés.

Le bonus (troisième serveur + deuxième lien inter-switch) réduirait encore davantage l'impact.

**6. Quel est le lien entre haute disponibilité et cybersécurité ?**  
La haute disponibilité (HA) assure que le service reste accessible en permanence, même en cas de panne ou d'attaque. En cybersécurité, la disponibilité est l'un des trois critères fondamentaux (CIA). Un système hautement disponible résiste mieux aux attaques par déni de service, aux pannes matérielles et aux erreurs humaines. La redondance est le mécanisme technique qui permet d'atteindre la HA.
