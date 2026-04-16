# TP : Système distribué et tolérance aux fautes

RSX102 - Technologies pour les applications en réseau  
Formateur : Boris Rose

---

## Plan d'adressage

| Équipement | Interface       | Adresse IP    | Masque        | Passerelle  |
|------------|-----------------|---------------|---------------|-------------|
| Routeur    | Gi0/0/0         | 192.168.1.1   | 255.255.255.0 | -           |
| Serveur1   | FastEthernet0   | 192.168.1.10  | 255.255.255.0 | 192.168.1.1 |
| Serveur2   | FastEthernet0   | 192.168.1.11  | 255.255.255.0 | 192.168.1.1 |
| PC1        | FastEthernet0   | 192.168.1.100 | 255.255.255.0 | 192.168.1.1 |
| PC2        | FastEthernet0   | 192.168.1.101 | 255.255.255.0 | 192.168.1.1 |

---

## Topologie

```
                  [ Routeur ISR 4331 ]
                  192.168.1.1/24
                 /  Gi0/0/0   Gi0/0/1 \
                /                      \
         [Switch1]----trunk----[Switch2]
          (2960)   Gi0/1-Gi0/1  (2960)
           /  \                  /  \
        Fa0/1 Fa0/2          Fa0/1 Fa0/2
         |      |              |      |
        PC1  Serveur1         PC2  Serveur2
```

Connexions :
- PC1 → Switch1 (Fa0/1)
- Serveur1 → Switch1 (Fa0/2)
- PC2 → Switch2 (Fa0/1)
- Serveur2 → Switch2 (Fa0/2)
- Switch1 → Routeur (Gi0/2 → Gi0/0/0)
- Switch2 → Routeur (Gi0/2 → Gi0/0/1)
- Switch1 ↔ Switch2 (Gi0/1 ↔ Gi0/1, trunk, redondance)

---

## Étapes de configuration

### 1. Routeur

Appliquer les fichiers :
- `routeur/host.config`
- `routeur/interfaces/switch1.config`
- `routeur/interfaces/switch2.config`

### 2. Switch1

Appliquer les fichiers :
- `switch1/host.config`
- `switch1/interfaces/routeur.config`
- `switch1/interfaces/switch2.config`
- `switch1/interfaces/pc1.config`
- `switch1/interfaces/serveur1.config`

### 3. Switch2

Appliquer les fichiers :
- `switch2/host.config`
- `switch2/interfaces/routeur.config`
- `switch2/interfaces/switch1.config`
- `switch2/interfaces/pc2.config`
- `switch2/interfaces/serveur2.config`

### 4. Serveurs (via GUI Packet Tracer)

Voir `serveur1/interface.config` et `serveur2/interface.config` :
- Desktop > IP Configuration : saisir IP, masque, passerelle
- Services > HTTP > ON
- Modifier `index.html` avec le message correspondant

### 5. PCs (via GUI Packet Tracer)

Voir `pc1/interface.config` et `pc2/interface.config` :
- Desktop > IP Configuration : saisir IP, masque, passerelle

---

## Tests

### Test système distribué (section 6)

Depuis PC1 (Desktop > Web Browser) :
```
http://192.168.1.10  -> affiche "Serveur distribue 1 actif"
http://192.168.1.11  -> affiche "Serveur distribue 2 actif"
```

Depuis PC2 :
```
http://192.168.1.10  -> affiche "Serveur distribue 1 actif"
http://192.168.1.11  -> affiche "Serveur distribue 2 actif"
```

Observation : plusieurs serveurs fournissent le même service -> système distribué.

### Test panne serveur (section 7)

1. Éteindre Serveur1 : clic sur Serveur1 > Physical > Power OFF
2. Depuis PC1, tester : `http://192.168.1.11`

Observation : le service reste disponible via Serveur2 -> tolérance aux fautes.

### Test panne réseau (section 8)

1. Déconnecter le câble entre Switch1 et Routeur
2. Depuis PC2, tester : `http://192.168.1.11`

Observation : PC2 → Switch2 → Routeur (chemin alternatif via Gi0/0/1) reste actif.
Le lien Switch1 ↔ Switch2 permet aussi d'atteindre Serveur1 sans passer par le routeur.

---

## Questions (section 10)

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

---

## BONUS (section 11)

Ajouts réalisés :
- **Serveur3** (192.168.1.12) connecté à Switch1 ou Switch2 avec HTTP ON et page "Serveur distribue 3 actif"
- **Deuxième lien inter-switch** : câble supplémentaire entre Switch1 (Gi0/3) et Switch2 (Gi0/3)

Observation : STP (Spanning Tree Protocol) bloque l'un des liens redondants pour éviter les boucles, et le réactive automatiquement si le lien actif tombe. Le réseau est plus robuste et la tolérance aux fautes augmente.
